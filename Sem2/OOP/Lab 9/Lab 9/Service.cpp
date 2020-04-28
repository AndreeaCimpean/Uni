#include "Service.h"
#include "MyExceptions.h"
#include "TextFileRepository.h"
#include "MemoryRepository.h"
#include <vector>
#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

std::vector<Evidence> Service::get_physical_copies_from_file() const
{
	if (this->physicalCopiesFile.find(".csv") != std::string::npos || this->physicalCopiesFile.find(".txt") != std::string::npos)
		return this->get_physical_copies_from_csv();
	else
		return this->get_physical_copies_from_html();
}

std::vector<Evidence> Service::get_physical_copies_from_csv() const
{
	ifstream input_file(this->physicalCopiesFile);
	vector<Evidence> physicalCopies;
	Evidence evidence;
	while (input_file >> evidence)
	{
		physicalCopies.push_back(evidence);
	}
	input_file.close();
	return physicalCopies;
}

std::vector<Evidence> Service::get_physical_copies_from_html() const
{
	vector<Evidence> physicalCopies;
	ifstream input_file(this->physicalCopiesFile);
	bool is_empty_file = (input_file.peek() == std::ifstream::traits_type::eof());
	if (is_empty_file)
		return physicalCopies;
	string line_read;
	for (int i = 1; i <= 15; ++i)
		getline(input_file, line_read);
	while (line_read != "</table>")
	{
		getline(input_file, line_read);
		int end = line_read.find("</td>");
		string id = line_read.substr(4, end - 4);

		getline(input_file, line_read);
		end = line_read.find("</td>");
		string measurement = line_read.substr(4, end - 4);

		getline(input_file, line_read);
		end = line_read.find("</td>");
		double imageClarityLevel = stod(line_read.substr(4, end - 4));

		getline(input_file, line_read);
		end = line_read.find("</td>");
		double quantity = stod(line_read.substr(4, end - 4));

		getline(input_file, line_read);
		int start = line_read.find("\">") + 2;
		end = line_read.find("</a>");
		string photograph = line_read.substr(start, end - start);
		
		Evidence evidence{ id, measurement, imageClarityLevel, quantity, photograph };
		physicalCopies.push_back(evidence);

		getline(input_file, line_read);
		getline(input_file, line_read);
	}
	return physicalCopies;
}

void Service::save_physical_copies_to_file(std::vector<Evidence> physicalCopies) const
{
	if (this->physicalCopiesFile.find(".csv") != std::string::npos || this->physicalCopiesFile.find(".txt") != std::string::npos)
		this->save_physical_copies_to_csv(physicalCopies);
	else
		this->save_physical_copies_to_html(physicalCopies);
}

void Service::save_physical_copies_to_html(std::vector<Evidence> physicalCopies) const
{
	this->write_html_header();
	this->write_html_body_begin();
	for (auto evidence : physicalCopies)
		evidence.to_html(physicalCopiesFile);
	this->write_html_body_end();
}

void Service::save_physical_copies_to_csv(std::vector<Evidence> physicalCopies) const
{
	ofstream output_file(this->physicalCopiesFile);
	for (auto evidence : physicalCopies)
		output_file << evidence << endl;
	output_file.close();
}

void Service::write_html_header() const
{
	ofstream output(this->physicalCopiesFile);
	output << "<!DOCTYPE html>" << endl;
	output << "<html>" << endl;
	output << "<head>" << endl;
	output << "<title>Evidences Database</title>" << endl;
	output << "</head>" << endl;
	output.close();
}

void Service::write_html_body_begin() const
{
	ofstream output(this->physicalCopiesFile, ios::app);
	output << "<body>" << endl;
	output << "<table border=\"1\">" << endl;
	output << "<tr>" << endl;
	output << "<td>Evidence Id</td>" << endl;
	output << "<td>Measurement</td>" << endl;
	output << "<td>Image Clarity Level</td>" << endl;
	output << "<td>Quantity</td>" << endl;
	output << "<td>Photograph</td>" << endl;
	output << "</tr>" << endl;
	output.close();
}

void Service::write_html_body_end() const
{
	ofstream output(this->physicalCopiesFile, ios::app);
	output << "</table>" << endl;
	output << "</body>" << endl;
	output << "</html>" << endl;
	output.close();
}

void Service::add_evidence(const Evidence& evidence)
{
	this->evidenceValidator.validate(evidence);
	this->repository.add_evidence(evidence);
}

void Service::update_evidence(const Evidence& evidence)
{
	/*
	Update an evidence in the list of evidences and in the physical copies as well
	*/
	this->evidenceValidator.validate(evidence);

	string id = evidence.get_id();
	string measurement = evidence.get_measurement();
	double imageClarityLevel = evidence.get_image_clarity_level();
	double quantity = evidence.get_quantity();
	string photograph = evidence.get_photograph();
	
	this->repository.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);

	vector<Evidence> physicalCopies = this->get_physical_copies_from_file();
	auto iterator_to_searched_evidence = std::find_if(physicalCopies.begin(), physicalCopies.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == physicalCopies.end())
		throw RepositoryException("Evidence does not exist!\n");
	int evidence_index = distance(physicalCopies.begin(), iterator_to_searched_evidence);
	physicalCopies[evidence_index].set_measurement(measurement);
	physicalCopies[evidence_index].set_image_clarity_level(imageClarityLevel);
	physicalCopies[evidence_index].set_quantity(quantity);
	physicalCopies[evidence_index].set_photograph(photograph);
	this->save_physical_copies_to_file(physicalCopies);
}

void Service::delete_evidence(const std::string& id)
{
	/*
	Delete an evidence from the list of evidences and from the physical copies as well
	*/
	this->repository.delete_evidence(id);
	
	vector<Evidence> physicalCopies = this->get_physical_copies_from_file();
	auto iterator_to_searched_evidence = std::find_if(physicalCopies.begin(), physicalCopies.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == physicalCopies.end())
		throw RepositoryException("Evidence does not exist!\n");
	physicalCopies.erase(iterator_to_searched_evidence);
	this->save_physical_copies_to_file(physicalCopies);
}

std::vector<Evidence> Service::get_evidences() const
{
	return this->repository.get_evidences();
}

int Service::get_number_of_evidences() const
{
	return this->repository.get_number_of_evidences();
}

Evidence Service::next_evidence()
{
	/*
	Return the next evidence to be displayed to the user
	*/
	return this->repository.next_evidence();
}

void Service::save_physical_copy(const std::string& id)
{
	/*
	Save a copy of an evidence in the list of physical copies
	parameter: id - the id of the evidence to be saved
	*/
	Evidence copy_evidence = this->repository.get_evidence_by_id(id);
	if (find_evidence_in_physical_copies_by_id(id) == 1)
		throw ServiceException("Evidence already saved!\n");
	if (this->physicalCopiesFile.find(".csv") != std::string::npos || this->physicalCopiesFile.find(".txt") != std::string::npos)
	{
		ifstream file(this->physicalCopiesFile);
		bool is_empty_file = (file.peek() == std::ifstream::traits_type::eof());
		file.close();
		ofstream output_file(this->physicalCopiesFile, ios::app);
		if (is_empty_file)
			output_file << copy_evidence;
		else
			output_file << endl << copy_evidence;
		output_file.close();
	}
	else
	{
		vector<Evidence>physicalCopies = this->get_physical_copies_from_html();
		physicalCopies.push_back(copy_evidence);
		this->save_physical_copies_to_html(physicalCopies);
	}
}

int Service::find_evidence_in_physical_copies_by_id(const std::string& id) const
{
	/*
	Find an evidence in the list of physical copies by its id
	Return:
		1 - if found
		0 - otherwise
	*/
	vector<Evidence> physicalCopies = this->get_physical_copies_from_file();
	auto iterator_to_searched_evidence = std::find_if(physicalCopies.begin(), physicalCopies.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == physicalCopies.end())
		return 0;
	else
		return 1;
}

const std::vector<Evidence>& Service::get_physical_copies() const
{
	return this->get_physical_copies_from_file();
}

int Service::get_number_of_physical_copies() const
{
	return this->get_physical_copies().size();
}

std::vector<Evidence> Service::filter_evidences_by_measurement_and_quantity(const std::string& measurement, const double quantity) const
{
	/*
	Filter evidences by measurement and quantity
	parameter: measurement - the exact measurement
			   quantity - the minimum quantity
	If measurement is empty or the quntity is -1 filter evidences only by the other condition
	Return: the filtered list
	*/
	vector<Evidence> filtered_list;
	vector<Evidence> evidences = this->get_evidences();
	if (measurement != "" && quantity != -1)
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_measurement() == measurement && evidence.get_quantity() >= quantity; });
	}
	else if (measurement == "")
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_quantity() >= quantity; });
	}
	else
	{
		copy_if(evidences.begin(), evidences.end(), back_inserter(filtered_list), [measurement, quantity](const Evidence evidence)->bool { return evidence.get_measurement() == measurement; });
	}
	return filtered_list;
}

void Service::set_repository_file(const std::string& file)
{
	/*
	Set the file name for the text repository
	parameter: file - the name of the file
	Set the file name, if the repository of the service is a text repository
	Throw an exception if the repository of teh service is not a text one
	*/
	try
	{
		TextFileRepository& text_repository = dynamic_cast<TextFileRepository&>(this->repository);
		text_repository.set_file_name(file);
	}
	catch (bad_cast)
	{
		throw ServiceException("Wrong repository type!\n");
	}
}

void Service::set_physical_copies_file(const std::string& file)
{
	this->physicalCopiesFile = file;
}

std::string Service::get_physical_copies_file() const
{
	return this->physicalCopiesFile;
}


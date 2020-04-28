#include "TextFileRepository.h"
#include "MyExceptions.h"
#include <fstream>
#include <vector>

using namespace std;

std::vector<Evidence> TextFileRepository::get_evidences_from_file() const
{
	/*
	Read evidences from the file of the text repository 
	Return the list of evidences read
	*/
	ifstream input_file(this->fileName);
	vector<Evidence> evidences;
	Evidence evidence;
	while (input_file >> evidence)
	{
		evidences.push_back(evidence);
	}
	input_file.close();
	return evidences;
}

void TextFileRepository::save_evidences_to_file(std::vector<Evidence> evidences) const
{
	/*
	Save a list of evidences to the file of the text repository
	parameter: evidences - list of the evidences to write in the file
	*/
	ofstream output_file(this->fileName);
	for (auto evidence : evidences)
		output_file << evidence << endl;
	output_file.close();
}

void TextFileRepository::add_evidence(const Evidence& evidence)
{
	/*
	Add an evidence to the text repository
	If the evidence already exists, throw an exception
	Write the evidence in the file of the repository otherwise
	*/
	if (!this->find_evidence_by_id(evidence.get_id()))
	{
		ifstream file(this->fileName);
		bool is_empty_file = (file.peek() == std::ifstream::traits_type::eof());
		file.close();
		ofstream output_file(this->fileName, ios::app);
		if (is_empty_file)
			output_file << evidence;
		else
			output_file << endl << evidence;
		output_file.close();
	}
	else
		throw RepositoryException("Duplicate evidence!\n");
}

int TextFileRepository::find_evidence_by_id(const std::string& id) const
{
	/*
	Find an evidence in the list of evidences by its id
	Return:
		1 - if found
		0 - otherwise
	*/
	vector<Evidence> evidences = this->get_evidences_from_file();
	auto iterator_to_searched_evidence = std::find_if(evidences.begin(), evidences.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == evidences.end())
		return 0;
	else
		return 1; }

void TextFileRepository::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const int quantity, const std::string& photograph)
{
	/*
	Update an evidence given by its id
	parmaeters: id - the evidence id
				measurement - the new measurement
				imageClarityLevel - the new image clarity level
				quantity - the new quantity
				phototgraph - the new phototgraph
	Update de evidence if it doesn't already exist
	Throw an exception otherwise
	*/
	vector<Evidence> evidences = this->get_evidences_from_file();
	auto iterator_to_searched_evidence = std::find_if(evidences.begin(), evidences.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == evidences.end())
		throw RepositoryException("Evidence does not exist!\n");
	
	int evidence_index = distance(evidences.begin(), iterator_to_searched_evidence);
	evidences[evidence_index].set_measurement(measurement);
	evidences[evidence_index].set_image_clarity_level(imageClarityLevel);
	evidences[evidence_index].set_quantity(quantity);
	evidences[evidence_index].set_photograph(photograph);
	this->save_evidences_to_file(evidences);
}

void TextFileRepository::delete_evidence(const std::string& id)
{
	/*
	Delete an evidence from the list of evidences
	parameter: id - the if of the the evidence to be deleted
	Delete the evidence if it doesn't already exists
	Throw an exception otherwise
	*/
	vector<Evidence> evidences = this->get_evidences_from_file();
	auto iterator_to_searched_evidence = std::find_if(evidences.begin(), evidences.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == evidences.end())
		throw RepositoryException("Evidence does not exist!\n");

	evidences.erase(iterator_to_searched_evidence);
	this->save_evidences_to_file(evidences);
}

std::vector<Evidence> TextFileRepository::get_evidences() const
{
	/*
	Get the list of all evidences
	*/
	return this->get_evidences_from_file();
}

int TextFileRepository::get_number_of_evidences() const
{
	int count = 0;
	ifstream input_file(this->fileName);
	Evidence evidence;
	while (input_file >> evidence)
		count++;
	input_file.close();
	return count;
}

Evidence TextFileRepository::next_evidence()
{
	/*
	Return the next evidence to be displayed for user
	*/
	vector<Evidence> evidences = this->get_evidences_from_file();
	Evidence evidence_before = evidences[this->evidencesIterator];
	this->evidencesIterator++;
	if (this->evidencesIterator == this->get_number_of_evidences())
		this->evidencesIterator = 0;
	return evidence_before;
}

Evidence TextFileRepository::get_evidence_by_id(const std::string& id) const
{
	/*
	Get an evidence by its id
	parameter: id - the id of the evidence
	return: the evidence if it exists
	Throw an exception otherwise
	*/
	vector<Evidence> evidences = this->get_evidences_from_file();
	auto iterator_to_searched_evidence = std::find_if(evidences.begin(), evidences.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator_to_searched_evidence == evidences.end())
		throw RepositoryException("Evidence does not exist!\n");
	int evidence_index = distance(evidences.begin(), iterator_to_searched_evidence);
	return evidences[evidence_index];
}

void TextFileRepository::set_file_name(const std::string& file)
{
	/*
	Set the file name of the text repository
	*/
	this->fileName = file;
}

std::string TextFileRepository::get_file_name() const
{
	/*
	Get the file name of the text repository
	*/
	return this->fileName;
}


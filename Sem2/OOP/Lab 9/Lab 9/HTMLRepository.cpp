#include "HTMLRepository.h"
#include <fstream>

std::vector<Evidence> HTMLRepository::get_evidences_from_file() const
{
	vector<Evidence> physicalCopies;
	ifstream input_file(this->fileName);
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

void HTMLRepository::save_evidences_to_file(std::vector<Evidence> physicalCopies) const
{
	this->write_html_header();
	this->write_html_body_begin();
	for (auto evidence : physicalCopies)
		evidence.to_html(this->fileName);
	this->write_html_body_end();
}

void HTMLRepository::write_html_header() const
{
	ofstream output(this->fileName);
	output << "<!DOCTYPE html>" << endl;
	output << "<html>" << endl;
	output << "<head>" << endl;
	output << "<title>Evidences Database</title>" << endl;
	output << "</head>" << endl;
	output.close();
}

void HTMLRepository::write_html_body_begin() const
{
	ofstream output(this->fileName, ios::app);
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

void HTMLRepository::write_html_body_end() const
{
	ofstream output(this->fileName, ios::app);
	output << "</table>" << endl;
	output << "</body>" << endl;
	output << "</html>" << endl;
	output.close();
}

void HTMLRepository::add_evidence(const Evidence& evidence)
{
	vector<Evidence>physicalCopies = this->get_evidences_from_file();
	physicalCopies.push_back(evidence);
	this->save_evidences_to_file(physicalCopies);
}

#include "UI.h"
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void UI::run()
{
	string mode;
	string command = "";
	cin >> command;
	while (command != "exit")
	{
		if (command == "mode")
		{
			cin.ignore();
			cin >> mode;
			if (mode != "A" && mode != "B")
				cout << "Invalid mode!";
		}
		else if (command == "add")
		{
			if (mode == "A")
			{
				string id, measurement, imageClarityLevel, quantity, photograph;
				this->read_evidence(id, measurement, imageClarityLevel, quantity, photograph);
				try
				{
					this->check_measurement(measurement);					
					this->check_image_clarity_level(imageClarityLevel);
					this->check_quantity(quantity);
					this->add_evidence(id, measurement, stod(imageClarityLevel), stod(quantity), photograph);
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "update")
		{
			if (mode == "A")
			{
				string id, measurement, imageClarityLevel, quantity, photograph;
				this->read_evidence(id, measurement, imageClarityLevel, quantity, photograph);
				try
				{
					this->check_measurement(measurement);
					this->check_image_clarity_level(imageClarityLevel);
					this->check_quantity(quantity);
					this->update_evidence(id, measurement, stod(imageClarityLevel), stod(quantity), photograph);
				}
				catch (const char* message)
				{
					cout << message << endl;
				}
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "delete")
		{
			if (mode == "A")
			{
				string id;
				cin.ignore();
				getline(cin, id);
				this->delete_evidence(id);
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "list")
		{
			if (mode == "A")
			{
				this->list_evidences();
			}
			else
			{
				string parameters_read;
				string measurement, quantity;
				cin.ignore();
				getline(cin, parameters_read);
				parameters_read.erase(remove(parameters_read.begin(), parameters_read.end(), ' '), parameters_read.end());
				int count_commas = count(parameters_read.begin(), parameters_read.end(), ',');
				if (count_commas == 1)
				{
					int index = 0;
					while (parameters_read[index] != ',')
						index++;
					measurement = parameters_read.substr(0, index);
					quantity = parameters_read.substr(index + 1);
					try
					{
						this->check_measurement(measurement);
						this->check_quantity(quantity);
						this->list_evidences_filtered_by_measurements_and_quantity(measurement, stod(quantity));
					}
					catch (const char* message)
					{
						cout << message;
					}
				}
				else
				{
					try
					{
						measurement = parameters_read;
						this->check_measurement(measurement);
						this->list_evidences_filtered_by_measurements_and_quantity(measurement, -1);
					}
					catch(...)
					{
						try
						{
							quantity = parameters_read;
							this->check_quantity(quantity);
							measurement = "";
							this->list_evidences_filtered_by_measurements_and_quantity(measurement, stod(quantity));
						}
						catch (...)
						{
							cout << "Invalid input!";

						}
					}
				}
			}
		}
		else if (command == "next")
		{
			if (mode == "B")
			{
				this->next_evidence();
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "save")
		{
			if (mode == "B")
			{
				string id;
				cin.ignore();
				cin >> id;
				this->save_physical_copy(id);
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "mylist")
		{
			if (mode == "B")
			{
				this->list_physical_copies();
			}
			else
				cout << "Wrong mode!";
		}
		else if (command != "exit")
			cout << "Wrong command!";
		cin >> command;
	}
}

void UI::check_measurement(const std::string& measurement) const
{
	int count_x = count(measurement.begin(), measurement.end(), 'X');
	if (count_x != 2)
		throw "Invalid measurement!";
	if (!isdigit(measurement[0]))
		throw "Invalid measurement!";
	for (int i = 1; i < measurement.length(); ++i)
	{
		if (!isdigit(measurement[i]))
		{
			if (measurement[i] != 'X' || (measurement[i] == 'X' && !isdigit(measurement[i - 1])))
				throw "Invalid measurement!";
		}
		else if (measurement[i] == '0' && measurement[i - 1] == 'X')
			throw "Invalid measurement!";
	}
}

void UI::check_image_clarity_level(const std::string& imageClarityLevel) const
{
	if (!isdigit(imageClarityLevel[0]))
		throw "Invalid image clarity level!";
	int count_dots = count(imageClarityLevel.begin(), imageClarityLevel.end(), '.');
	if (count_dots != 0 && count_dots != 1)
		throw "Invalid image clarity level!";
	for (int i = 0; i < imageClarityLevel.length(); ++i)
		if (!isdigit(imageClarityLevel[i]) && imageClarityLevel[i] != '.')
			throw "Invalid image clarity level!";
}

void UI::check_quantity(const std::string& quantity) const
{
	if (!isdigit(quantity[0]))
		throw "Invalid quantity!";
	int count_dots = count(quantity.begin(), quantity.end(), '.');
	if (count_dots != 0 && count_dots != 1)
		throw "Invalid quantity!";
	for (int i = 0; i < quantity.length(); ++i)
		if (!isdigit(quantity[i]) && quantity[i] != '.')
			throw "Invalid quantity!";
}

void UI::add_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph)
{
	try
	{
		this->service.add_evidence(id, measurement, imageClarityLevel, quantity, photograph);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::read_evidence(std::string& id, std::string& measurement, std::string& imageClarityLevel, std::string& quantity, std::string& photograph) const
{
	string parameters_read;
	getline(cin, parameters_read);
	parameters_read.erase(remove(parameters_read.begin(), parameters_read.end(), ' '), parameters_read.end());
	int index = 0, previous_index;
	while (parameters_read[index] != ',')
		index++;
	id = parameters_read.substr(0, index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	measurement = parameters_read.substr(previous_index, index - previous_index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	imageClarityLevel = parameters_read.substr(previous_index, index - previous_index);
	index += 1;
	previous_index = index;

	while (parameters_read[index] != ',')
		index++;
	quantity = parameters_read.substr(previous_index, index - previous_index);

	photograph = parameters_read.substr(index + 1);
}

void UI::update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph)
{
	try
	{
		this->service.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::delete_evidence(const std::string& id)
{	
	try
	{
		this->service.delete_evidence(id);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::list_evidences() const
{
	Evidence* evidences =  this->service.get_evidences();
	for (int i = 0; i < this->service.get_number_of_evidences(); ++i)
	{
		Evidence current_evidence = *(evidences + i);
		cout << "Id: "<< current_evidence.get_id() << " Measurement: "<<current_evidence.get_measurement()<<" Image clarity level: " << current_evidence.get_image_clarity_level() <<" Quantity: "<< current_evidence.get_quantity() <<" Photograph: "<< current_evidence.get_photograph()<<endl;
	}
}

void UI::next_evidence()
{
	Evidence next_evidence = this->service.next_evidence();
	cout << "Id: " << next_evidence.get_id() << " Measurement: " << next_evidence.get_measurement() << " Image clarity level: " << next_evidence.get_image_clarity_level() << " Quantity: " << next_evidence.get_quantity() << " Photograph: " << next_evidence.get_photograph() << endl;
}

void UI::save_physical_copy(const std::string& id)
{
	try
	{
		this->service.save_physical_copy(id);
	}
	catch(const char* message)
	{
		cout << message;
	}
}

void UI::list_physical_copies()
{
	Evidence* physical_copies = this->service.get_physical_copies();
	int number_of_physical_copies = this->service.get_number_of_physical_copies();
	for (int i = 0; i < number_of_physical_copies; ++i)
	{
		Evidence current_evidence = *(physical_copies + i);
		cout << "Id: " << current_evidence.get_id() << " Measurement: " << current_evidence.get_measurement() << " Image clarity level: " << current_evidence.get_image_clarity_level() << " Quantity: " << current_evidence.get_quantity() << " Photograph: " << current_evidence.get_photograph() << endl;
	}
	this->service.get_physical_copies();
}

void UI::list_evidences_filtered_by_measurements_and_quantity(const std::string& measurement, double quantity)
{
	Evidence filtered_list[MAX_DIMENSION_LIST_EVIDENCES];
	int length_filtered_list = 0;
	this->service.filter_evidences_by_measurement_and_quantity(filtered_list, length_filtered_list, measurement, quantity);
	for (int i = 0; i < length_filtered_list; ++i)
	{
		Evidence current_evidence = filtered_list[i];
		cout << "Id: " << current_evidence.get_id() << " Measurement: " << current_evidence.get_measurement() << " Image clarity level: " << current_evidence.get_image_clarity_level() << " Quantity: " << current_evidence.get_quantity() << " Photograph: " << current_evidence.get_photograph() << endl;
	}
}

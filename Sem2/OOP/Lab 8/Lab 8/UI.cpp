#include "UI.h"
#include "Evidence.h"
#include "Validations.h"
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
		if (command == "fileLocation")
		{
			string file;
			cin.ignore();
			getline(cin, file);
			this->set_file(file);
		}
		else if (command == "mode")
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
				try
				{
					Evidence evidence{};
					cin.ignore();
					cin >> evidence;
					this->add_evidence(evidence);
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
				Evidence evidence{};
				try
				{
					cin.ignore();
					cin >> evidence;
					this->update_evidence(evidence);
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
						check_measurement(measurement);
						check_quantity(quantity);
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
						check_measurement(measurement);
						this->list_evidences_filtered_by_measurements_and_quantity(measurement, -1);
					}
					catch(...)
					{
						try
						{
							quantity = parameters_read;
							check_quantity(quantity);
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

void UI::add_evidence(const Evidence& evidence)
{
	try
	{
		this->service.add_evidence(evidence);
	}
	catch (const char* message)
	{
		cout << message << endl;
	}
}

void UI::update_evidence(const Evidence& evidence)
{
	try
	{
		this->service.update_evidence(evidence.get_id(), evidence.get_measurement(), evidence.get_image_clarity_level(), evidence.get_quantity(), evidence.get_photograph());
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
	vector<Evidence> evidences = this->service.get_evidences();
	for_each(evidences.begin(), evidences.end(), [](Evidence evidence) {cout << evidence << endl; });
}

void UI::next_evidence()
{
	Evidence next_evidence = this->service.next_evidence();
	cout << next_evidence << endl;
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

void UI::list_physical_copies() const
{
	vector<Evidence> physical_copies = this->service.get_physical_copies();
	for_each(physical_copies.begin(), physical_copies.end(), [](Evidence evidence) {cout << evidence << endl; });
}

void UI::list_evidences_filtered_by_measurements_and_quantity(const std::string& measurement, double quantity) const
{
	vector<Evidence> filtered_list;
	this->service.filter_evidences_by_measurement_and_quantity(filtered_list, measurement, quantity);
	for (auto evidence : filtered_list)
	{
		cout << evidence << endl;
	}
}

void UI::set_file(const std::string& file)
{
	try
	{
		this->service.set_file(file);
	}
	catch (const char* message)
	{
		cout << message;
	}
}

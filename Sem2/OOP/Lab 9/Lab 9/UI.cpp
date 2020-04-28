#include "UI.h"
#include "Evidence.h"
#include <iostream>
#include <string>
#include <algorithm>
#include <Windows.h>
#include <shellapi.h>

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
			this->set_repository_file(file);
		}
		else if (command == "mylistLocation")
		{
			string file;
			cin.ignore();
			getline(cin, file);
			this->set_physical_copies_file(file);
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
				Evidence evidence{};
				cin.ignore();
				try
				{
					cin >> evidence;
				}
				catch (exception& exception)
				{
					cout << exception.what();
				}
				this->add_evidence(evidence);
			}
			else
				cout << "Wrong mode!";
		}
		else if (command == "update")
		{
			if (mode == "A")
			{
				Evidence evidence{};
				cin.ignore();
				try
				{
					cin >> evidence;
				}
				catch (exception& exception)
				{
					cout << exception.what();
				}
				this->update_evidence(evidence);
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
					this->list_evidences_filtered_by_measurements_and_quantity(measurement, stod(quantity));
				}
				else
				{
					int count_x = count(parameters_read.begin(), parameters_read.end(), 'X');
					if (count_x == 1)
						this->list_evidences_filtered_by_measurements_and_quantity(measurement, -1);
					else
							this->list_evidences_filtered_by_measurements_and_quantity(measurement, stod(quantity));
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
	catch (const exception& exception)
	{
		cout<< exception.what();
	}
}

void UI::update_evidence(const Evidence& evidence)
{
	try
	{
		this->service.update_evidence(evidence);
	}
	catch (const exception& exception)
	{
		cout << exception.what();
	}
}

void UI::delete_evidence(const std::string& id)
{	
	try
	{
		this->service.delete_evidence(id);
	}
	catch (const exception& exception)
	{
		cout << exception.what();
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
	catch (const exception& exception)
	{
		cout << exception.what();
	}
}

void UI::list_physical_copies() const
{
	string file = this->service.get_physical_copies_file();
	file.insert(0,"\"");
	file+="\"";
	if (file.find(".csv") != std::string::npos)
		ShellExecuteA(NULL, NULL, "notepad++.exe", file.c_str(), NULL, SW_SHOWMAXIMIZED);
	else
		ShellExecuteA(NULL, NULL, "chrome.exe", file.c_str(), NULL, SW_SHOWMAXIMIZED);
	vector<Evidence> physical_copies = this->service.get_physical_copies();
	for_each(physical_copies.begin(), physical_copies.end(), [](Evidence evidence) {cout << evidence << endl; });
}

void UI::list_evidences_filtered_by_measurements_and_quantity(const std::string& measurement, double quantity) const
{
	vector<Evidence> filtered_list;
	filtered_list = this->service.filter_evidences_by_measurement_and_quantity(measurement, quantity);
	for (auto evidence : filtered_list)
	{
		cout << evidence << endl;
	}
}

void UI::set_repository_file(const std::string& file)
{
	try
	{
		this->service.set_repository_file(file);
	}
	catch (const exception& exception)
	{
		cout << exception.what();
	}
}

void UI::set_physical_copies_file(const std::string& file)
{
	this->service.set_physical_copies_file(file);
}

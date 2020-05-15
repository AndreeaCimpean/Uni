#include "Service.h"
#include "TextFileRepository.h"
#include "MemoryRepository.h"
#include "Validations.h"
#include <algorithm>
#include "ActionAdd.h"
#include "ActionRemove.h"
#include "ActionUpdate.h"

using namespace std;

void Service::add_evidence(const Evidence& evidence)
{
	this->repository.add_evidence(evidence);
	unique_ptr<Action> actionUndo = make_unique<ActionAdd>(evidence, this->repository);
	this->undoStack.push_back(move(actionUndo));
}

void Service::update_evidence(const std::string& id, const std::string& measurement, double imageClarityLevel, double quantity, const std::string& photograph)
{
	/*
	Update an evidence in the list of evidences and in the physical copies as well
	*/
	Evidence evidence_before = this->get_evidence_by_id(id);

	this->repository.update_evidence(id, measurement, imageClarityLevel, quantity, photograph);

	Evidence evidence_after = this->get_evidence_by_id(id);
	unique_ptr<Action> actionUndo = make_unique<ActionUpdate>(evidence_before, evidence_after, this->repository);
	this->undoStack.push_back(move(actionUndo));

	int evidence_index = this->find_evidence_index_in_physical_copies_by_id(id);
	if (evidence_index != -1)
	{
		this->physicalCopies[evidence_index].set_measurement(measurement);
		this->physicalCopies[evidence_index].set_image_clarity_level(imageClarityLevel);
		this->physicalCopies[evidence_index].set_quantity(quantity);
		this->physicalCopies[evidence_index].set_photograph(photograph);
	}
}

void Service::delete_evidence(const std::string& id)
{
	/*
	Delete an evidence from the list of evidences and from the physical copies as well
	*/
	Evidence evidence_before = this->get_evidence_by_id(id);
	this->repository.delete_evidence(id);

	unique_ptr<Action> actionUndo = make_unique<ActionRemove>(evidence_before, this->repository);
	this->undoStack.push_back(move(actionUndo));

	int evidence_index= this->find_evidence_index_in_physical_copies_by_id(id);
	if (evidence_index != -1)
		this->physicalCopies.erase(this->physicalCopies.begin() + evidence_index);
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
	this->physicalCopies.push_back(copy_evidence);
}

int Service::find_evidence_index_in_physical_copies_by_id(const std::string& id) const
{
	/*
	Find an evidence in the list of physical copies
	parameter: id - the id of the evidence
	return:
		-1 if evidence if not found
		its index in the list otherwise
	*/
	auto iterator = std::find_if(this->physicalCopies.begin(), this->physicalCopies.end(), [id](const Evidence evidence) {return evidence.get_id() == id; });
	if (iterator == this->physicalCopies.end())
		return -1;
	else
		return std::distance(this->physicalCopies.begin(), iterator); }

const std::vector<Evidence>& Service::get_physical_copies() const
{
	return this->physicalCopies;
}

int Service::get_number_of_physical_copies() const
{
	return this->physicalCopies.size();
}

void Service::filter_evidences_by_measurement_and_quantity(vector<Evidence>& filtered_list, const std::string& measurement, const double quantity) const
{
	/*
	Filter evidences by measurement and quantity
	parameter: filtered_list - the list used to return the filtered evidences
			   measurement - the exact measurement
			   quantity - the minimum quantity
	If measurement is empty or the quntity is -1 filter evidences only by the other condition
	*/
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
}

void Service::set_file(const std::string& file)
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
		throw "Wrong repository type!"; }
}

Evidence Service::get_evidence_by_id(const std::string& id)
{
	return this->repository.get_evidence_by_id(id);
}

void Service::undo()
{
	if (this->undoStack.size() == 0)
		throw "No more undos! ";
	this->undoStack.back()->execute_undo();
	this->redoStack.push_back(move(undoStack.back()));
	this->undoStack.pop_back();
}

void Service::redo()
{
	if (this->redoStack.size() == 0)
		throw "No more redos! ";
	this->redoStack.back()->execute_redo();
	this->undoStack.push_back(move(this->redoStack.back()));
	this->redoStack.pop_back();
}


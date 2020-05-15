#include "ActionUpdate.h"

using namespace std;

void ActionUpdate::execute_undo()
{
	string id = evidenceBefore.get_id();
	string measurments = evidenceBefore.get_measurement();
	double quantity = evidenceBefore.get_quantity();
	double imageClarityLevel = evidenceBefore.get_image_clarity_level();
	string phototgraph = evidenceBefore.get_photograph();
	this->repository.update_evidence(id, measurments, imageClarityLevel, quantity, phototgraph);
}

void ActionUpdate::execute_redo()
{
	string id = evidenceAfter.get_id();
	string measurments = evidenceAfter.get_measurement();
	double quantity = evidenceAfter.get_quantity();
	double imageClarityLevel = evidenceAfter.get_image_clarity_level();
	string phototgraph = evidenceAfter.get_photograph();
	this->repository.update_evidence(id, measurments, imageClarityLevel, quantity, phototgraph);
}

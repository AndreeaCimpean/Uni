#include "ActionAdd.h"

void ActionAdd::execute_undo()
{
	this->repository.delete_evidence(this->addedEvidence.get_id());
}

void ActionAdd::execute_redo()
{
	this->repository.add_evidence(this->addedEvidence);
}

#include "ActionRemove.h"

void ActionRemove::execute_undo()
{
	this->repository.add_evidence(this->deletedEvidence);
}

void ActionRemove::execute_redo()
{
	this->repository.delete_evidence(this->deletedEvidence.get_id());
}

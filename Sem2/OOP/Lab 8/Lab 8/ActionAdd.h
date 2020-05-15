#pragma once
#include "Action.h"
#include "Evidence.h"
#include "RepositoryInterafce.h"

class ActionAdd : public Action 
{
private:
	Evidence addedEvidence;
	RepositoryInterface& repository;
public:
	ActionAdd(const Evidence& evidence, RepositoryInterface& repository) : addedEvidence{ evidence }, repository{repository} {};
	void execute_undo() override;
	void execute_redo() override;
};


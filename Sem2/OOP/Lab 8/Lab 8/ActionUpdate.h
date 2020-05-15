#pragma once
#include "Action.h"
#include "RepositoryInterafce.h"
#include "Evidence.h"

class ActionUpdate : public Action
{
private:
	Evidence evidenceBefore;
	Evidence evidenceAfter;
	RepositoryInterface& repository;
public:
	ActionUpdate(const Evidence& evidenceBefore, const Evidence& evidenceAfter, RepositoryInterface& repository) : evidenceBefore{ evidenceBefore }, evidenceAfter{ evidenceAfter }, repository{ repository }{};
	void execute_undo() override;
	void execute_redo() override;
};


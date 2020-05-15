#pragma once
#include "Service.h"

class UI
{
private:
	Service& service;
public:
	UI(Service& service) : service{service} {}
	void run();
	void add_evidence(const Evidence& evidence);
	void update_evidence(const Evidence& evidence);
	void delete_evidence(const std::string& id);
	void list_evidences() const;
	void next_evidence();
	void save_physical_copy(const std::string& id);
	void list_physical_copies() const;
	void list_evidences_filtered_by_measurements_and_quantity(const std::string& measurement, double quantity) const;
	void set_file(const std::string& file);
	void undo();
	void redo();
};


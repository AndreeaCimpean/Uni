#pragma once
#include "RepositoryInterafce.h"
#include "Evidence.h"
#include "EvidenceValidator.h"

class Service
{
private:
	std::string physicalCopiesFile;
	EvidenceValidator& evidenceValidator;
	Repository& repository;
	std::vector<Evidence> get_physical_copies_from_file() const;
	std::vector<Evidence> get_physical_copies_from_csv() const;
	std::vector<Evidence> get_physical_copies_from_html() const;
	void save_physical_copies_to_file(std::vector<Evidence> physicalCopies) const;
	void save_physical_copies_to_html(std::vector<Evidence> physicalCopies) const;
	void save_physical_copies_to_csv(std::vector<Evidence> physicalCopies) const;
	void write_html_header() const;
	void write_html_body_begin() const;
	void write_html_body_end() const;
public:
	Service(EvidenceValidator& evidenceValidator, Repository& repository) : evidenceValidator{ evidenceValidator }, repository{ repository } {};
	void add_evidence(const Evidence& evidence);
	void update_evidence(const Evidence& evidence);
	void delete_evidence(const std::string& id);
	std::vector<Evidence> get_evidences() const;
	int get_number_of_evidences() const;
	Evidence next_evidence();
	void save_physical_copy(const std::string& id);
	int find_evidence_in_physical_copies_by_id(const std::string& id) const;
	const std::vector<Evidence>& get_physical_copies() const;
	int get_number_of_physical_copies() const;
	std::vector<Evidence> filter_evidences_by_measurement_and_quantity(const std::string& measurement, const double quantity) const;
	void set_repository_file(const std::string& file);
	void set_physical_copies_file(const std::string& file);
	std::string get_physical_copies_file() const;
};


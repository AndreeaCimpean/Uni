#pragma once
#include "RepositoryInterafce.h"
#include "TextFileRepository.h"
#include "HTMLRepository.h"
#include "Evidence.h"
#include "EvidenceValidator.h"
#include <memory>

class Service
{
private:
	EvidenceValidator& evidenceValidator;
	Repository& repository;
	TextFileRepository* physicalCopiesRepository;
public:
	Service(EvidenceValidator& evidenceValidator, Repository& repository, TextFileRepository& text) : evidenceValidator{ evidenceValidator }, repository{ repository }, physicalCopiesRepository{ physicalCopiesRepository }{};
	void add_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph);
	void update_evidence(const std::string& id, const std::string& measurement, const double imageClarityLevel, const double quantity, const std::string& photograph);
	void delete_evidence(const std::string& id);
	std::vector<Evidence> get_evidences() const;
	int get_number_of_evidences() const;
	Evidence next_evidence();
	void save_physical_copy(const std::string& id);
	int find_evidence_in_physical_copies_by_id(const std::string& id) const;
	const std::vector<Evidence> get_physical_copies() const;
	int get_number_of_physical_copies() const;
	std::vector<Evidence> filter_evidences_by_measurement_and_quantity(const std::string& measurement, const double quantity) const;
	void set_repository_file(const std::string& file);
	void set_physical_copies_file(const std::string& file);
	std::string get_physical_copies_file() const;
	void set_physical_copies_repository(TextFileRepository* repository);
};


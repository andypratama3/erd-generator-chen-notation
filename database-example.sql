-- ======================================================
-- SIMPLE DATABASE - 5 RELATED TABLES
-- ======================================================
-- Contoh: Sistem Manajemen Karyawan, Departemen, & Proyek
-- ======================================================

-- 1. DEPARTMENTS (Master Table - No Dependencies)
CREATE TABLE `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `code` varchar(10) NOT NULL,
  `location` varchar(100) DEFAULT NULL,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. POSITIONS (Master Table - No Dependencies)
CREATE TABLE `positions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `level` int NOT NULL,
  `description` text,
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. EMPLOYEES (Detail Table - FK to departments & positions)
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `hire_date` date NOT NULL,
  `department_id` int NOT NULL,
  `position_id` int NOT NULL,
  `salary` decimal(12,2) DEFAULT NULL,
  `status` enum('active','inactive','resigned') DEFAULT 'active',
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `department_id` (`department_id`),
  KEY `position_id` (`position_id`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE RESTRICT,
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 4. PROJECTS (Detail Table - FK to departments)
CREATE TABLE `projects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `code` varchar(20) NOT NULL,
  `description` text,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `budget` decimal(15,2) DEFAULT NULL,
  `department_id` int NOT NULL,
  `status` enum('planning','active','completed','cancelled') DEFAULT 'planning',
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `code` (`code`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 5. PROJECT_ASSIGNMENTS (Junction Table - M:N between employees & projects)
CREATE TABLE `project_assignments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int NOT NULL,
  `project_id` int NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  `assigned_date` date NOT NULL,
  `hours_allocated` decimal(5,2) DEFAULT NULL,
  `status` enum('assigned','active','completed','removed') DEFAULT 'assigned',
  `created_at` timestamp DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_assignment` (`employee_id`, `project_id`),
  KEY `employee_id` (`employee_id`),
  KEY `project_id` (`project_id`),
  CONSTRAINT `project_assignments_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`) ON DELETE CASCADE,
  CONSTRAINT `project_assignments_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

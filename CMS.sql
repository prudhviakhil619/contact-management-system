

CREATE TABLE `user` (
  user_id int NOT NULL,
  user_name varchar(30) NOT NULL,
  user_mobile INT NOT NULL,
  user_email varchar(30) NOT NULL,
  user_address varchar(45) NOT NULL ,
  role_id INT NOT NULL,
  per_id INT NOT NULL,
  login_id int NOT NULL,
  ssn_num varchar(9) NOT NULL,
  PRIMARY KEY (`user_id`),
  FOREIGN KEY (role_id) REFERENCES ROLES(role_id),
  FOREIGN KEY (login_id) REFERENCES login(login_id),
  FOREIGN KEY (per_id) REFERENCES PERMISSION(per_id));
  
  
  
CREATE TABLE `roles` (
  role_id INT NOT NULL,
  role_name varchar(45) NOT NULL ,
  role_desc varchar(45) NOT NULL ,
  PRIMARY KEY (`role_id`));
  
  
  
  CREATE TABLE `customer` (
  cus_id int NOT NULL,
  cus_name varchar(45) NOT NULL,
  cus_mobile INT NOT NULL,
  cus_email varchar(45) NOT NULL,
  cus_dob varchar(45) NOT NULL,
  cus_age varchar(9) NOT NULL,
  com_id  INT NOT NULL,
  PRIMARY KEY (`cus_id`),
  FOREIGN KEY (com_id) REFERENCES company(com_id));
  
  
  CREATE TABLE `permission` (
  per_id INT  NOT NULL,
  per_role_id varchar(45) NOT NULL,
  per_module varchar(45) NOT NULL,
  per_name varchar(45) NOT NULL,
  PRIMARY KEY (`per_id`)); 
  
  
  
  CREATE TABLE `login` (
  login_id int NOT NULL,
  login_username varchar(45) NOT NULL,
  login_password varchar(45) NOT NULL,
  PRIMARY KEY (`login_id`));
  
  
  
  CREATE TABLE `manage` (
  cus_id int NOT NULL,
  cus_name varchar(45) NOT NULL,
  email_id varchar(45) NOT NULL,
  add_place varchar(45) NOT NULL,
  com_id INT NOT NULL,
  mob_num int NOT NULL,
  user_id INT NOT NULL,
  FOREIGN KEY (cus_id) REFERENCES customer(cus_id),
  FOREIGN KEY (email_id) REFERENCES email(email_id),
  FOREIGN KEY (add_place) REFERENCES address(add_place),
  FOREIGN KEY (com_id) REFERENCES company(com_id),
  FOREIGN KEY (com_id) REFERENCES company(com_id),
  FOREIGN KEY (mob_num) REFERENCES contacts(mob_num),
  FOREIGN KEY (user_id) REFERENCES user(user_id));
    
  
  
  CREATE TABLE `contacts` (
  mob_num int NOT NULL,
  con_des varchar(45) NOT NULL, 
  PRIMARY KEY (`mob_num`));
  
 
  
  CREATE TABLE `mobile` (
  mob_num int NOT NULL,
  mob_type varchar(45) NOT NULL ,
  FOREIGN KEY (mob_num) REFERENCES contacts(mob_num));
  

  
  CREATE TABLE `company` (
  com_id int NOT NULL,
  com_name varchar(45) NOT NULL,
  com_email varchar(45) NOT NULL,
  com_add varchar(45) NOT NULL,
  com_num int NOT NULL,
  PRIMARY KEY (`com_id`)); 
  
  
  CREATE TABLE `address` (
  add_place varchar(45) NOT NULL,
  add_desc varchar(45) NOT NULL,
  PRIMARY KEY (`add_place`));
  

  
  CREATE TABLE `email` (
  email_id varchar(45) NOT NULL,
  office_email varchar(45) NOT NULL,
  PRIMARY KEY (`email_id`));
   



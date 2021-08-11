  
CREATE DATABASE `flask_mysql`;

USE `flask_mysql`;

create table `tareas`(
    `idTarea` int(11) not null AUTO_INCREMENT,
    `titulo` varchar(70) not null,
    `descripcion` varchar(100),
    `estado` int(11),
    `idUsuario` int(11) default null,
    PRIMARY KEY (`idTarea`)
)


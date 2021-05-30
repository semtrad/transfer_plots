DROP TABLE IF EXISTS `transfer_plots`;

CREATE TABLE `transfer_plots` (
  `id`                  int(11)       NOT NULL AUTO_INCREMENT,
  `from_hostname`       varchar(12)   DEFAULT NULL,
  `from_path`           varchar(255)  DEFAULT NULL,
  `plot_name`           varchar(255)  DEFAULT NULL,
  `plot_size`           int           DEFAULT NULL,
  `to_path`             varchar(255)  DEFAULT null,
  `status`              varchar(12)   DEFAULT NULL,
  `trasferred`          int           DEFAULT NULL,
  `update_datetime`     timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `article_id_phrase_id` (`plot_name`)
) ENGINE=InnoDB;

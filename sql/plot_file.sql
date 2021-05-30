DROP TABLE IF EXISTS `plot_file`;

CREATE TABLE `plot_file` (
  `id`                  int(11)       NOT NULL AUTO_INCREMENT,
  `from_hostname`       varchar(12)   DEFAULT NULL,
  `plot_name`           varchar(255)  DEFAULT NULL,
  `plot_size`           bigint        DEFAULT NULL,
  `to_path`             varchar(255)  DEFAULT null,
  `status`              varchar(12)   DEFAULT NULL,
  `transfer_start_time` datetime      DEFAULT NULL,
  `transfer_end_time`   datetime      DEFAULT NULL,
  `transfer_total_time` bigint        DEFAULT NULL,
  `update_datetime`     timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `article_id_phrase_id` (`plot_name`)
) ENGINE=InnoDB;

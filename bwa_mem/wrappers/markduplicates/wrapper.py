__author__ = "Johannes Köster"
__copyright__ = "Copyright 2016, Johannes Köster"
__email__ = "koester@jimmy.harvard.edu"
__license__ = "MIT"


from snakemake.shell import shell


shell(
    "java -jar /shahlab/pipelines/apps_centos6/picard-tools-1.141/picard.jar MarkDuplicates {snakemake.params} INPUT={snakemake.input} "
    "OUTPUT={snakemake.output.bam} METRICS_FILE={snakemake.output.metrics} "
)
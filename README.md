# SONIA

SONIA is a python 3.6/2.7 software developed to infer selection pressures on features of amino acid CDR3 sequences. The inference is based on maximizing the likelihood of observing a selected data sample given a representative pre-selected sample. This method was first used in Elhanati et al (2014) to study thymic selection. For this purpose, the pre-selected sample can be generated internally using the OLGA software package, but SONIA allows it also to be supplied externally, in the same way the data sample is provided.

![](docs/source/model.png)

SONIA takes as input TCR CDR3 amino acid sequences, with or without per sequence lists of possible V and J genes suspected to be used in the recombination process for this sequence. Its output is selection factors for each amino acid ,(relative) position , CDR3 length combinations, and also for each V and J gene choice. These selection factors can be used to calculate sequence level selection factors which indicate how more or less represented this sequence would be in the selected pool as compared to the the pre-selected pool. These in turn could be used to calculate the probability to observe any sequence after selection and sample from the selected repertoire. 

![](docs/source/workflow.png)
## Version
Latest released version: 0.0.45

## Installation
SONIA is a python 2.7/3.6 software. It is available on PyPI and can be downloaded and installed through pip:

 ```pip install sonia```.

SONIA is also available on [GitHub](https://github.com/statbiophys/SONIA). The command line entry points can be installed by using the setup.py script:

 ```python setup.py install```.
 
Sometimes pip fails to install the dependencies correctly. Thus, if you get any error try first to install the dependencies separately:
 ```
pip install tensorflow
pip install matplotlib
pip install olga
pip install sonia 
 ```

## References

1. Sethna Z, Isacchini G, Dupic T, Mora T, Walczak AM, Elhanati Y, Population variability in the generation and thymic selection of T-cell repertoires, (2020) bioRxiv, https://doi.org/10.1101/2020.01.08.899682
2. Isacchini G, Sethna Z, Elhanati Y ,Nourmohammad A, Mora T, Walczak AM, Generative models of T-cell receptor sequences, (2020) Phys. Rev. E 101, 062414, https://journals.aps.org/pre/abstract/10.1103/PhysRevE.101.062414
3. Elhanati Y, Murugan A , Callan CGJ ,  Mora T , Walczak AM, Quantifying selection in immune receptor repertoires, PNAS July 8, 2014 111 (27) 9875-9880, https://doi.org/10.1073/pnas.1409572111

## Documentation

Extensive documentation can be found [here](https://sonia-package.readthedocs.io/en/latest/)

## Contact

Any issues or questions should be addressed to [us](mailto:zachary.sethna@gmail.com,giulioisac@gmail.com).

## License

Free use of SONIA is granted under the terms of the GNU General Public License version 3 (GPLv3).
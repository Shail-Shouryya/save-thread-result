# https://pypi.org/classifiers/
# https://pypi.org/pypi?%3Aaction=list_classifiers
# https://test.pypi.org/pypi?%3Aaction=list_classifiers
# https://github.com/pypa/sampleproject/blob/master/setup.py
# https://packaging.python.org/guides/distributing-packages-using-setuptools/
from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


setup(
    # Different Python projects may use different versioning schemes based on the needs of that particular project, but all of them are required to comply with the flexible public version scheme specified in PEP 440 in order to be supported in tools and libraries like pip and setuptools.
    # Here are some examples of compliant version numbers:
    # 1.2.0.dev1  # Development release
    # 1.2.0a1     # Alpha Release
    # 1.2.0b1     # Beta Release
    # 1.2.0rc1    # Release Candidate
    # 1.2.0       # Final Release
    # 1.2.0.post1 # Post Release
    # 15.10       # Date based release
    # 23          # Serial release
    # To further accommodate historical variations in approaches to version numbering, PEP 440 also defines a comprehensive technique for version normalisation that maps variant spellings of different version numbers to a standardised canonical form.
    # Scheme choices
    # Semantic versioning (preferred)
    # For new projects, the recommended versioning scheme is based on Semantic Versioning, but adopts a different approach to handling pre-releases and build metadata.
    # The essence of semantic versioning is a 3-part MAJOR.MINOR.MAINTENANCE numbering scheme, where the project author increments:
    # 1. MAJOR version when they make incompatible API changes,
    # 2. MINOR version when they add functionality in a backwards-compatible manner, and
    # 3. MAINTENANCE version when they make backwards-compatible bug fixes.
    # Adopting this approach as a project author allows users to make use of “compatible release” specifiers, where name ~= X.Y requires at least release X.Y, but also allows any later release with a matching MAJOR version.
    # Python projects adopting semantic versioning should abide by clauses 1-8 of the Semantic Versioning 2.0.0 specification: https://semver.org/.
    version                       = '0.0.7',
    name                          = 'save-thread-result',
    description                   = 'Simple subclass wrapper around `threading.Thread` to get the return value from a thread in python. Exact same interface as `threading.Thread`! 🌟 Star this repo if you found it useful! 🌟',
    long_description              = long_description,
    long_description_content_type = 'text/markdown',
    url                           = 'https://github.com/slow-but-steady/save-thread-result/tree/main/python',
    author                        = 'slow-but-steady',
    author_email                  = 'slowbutsteady1234@gmail.com',
    license                       = 'Apache License 2.0',


    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: OpenStack',
        'Environment :: Other Environment',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Buffet',
        'Environment :: Web Environment :: Mozilla',
        'Environment :: Web Environment :: ToscaWidgets',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: Gnome',
        'Environment :: X11 Applications :: KDE',
        'Environment :: X11 Applications :: Qt',
        'Framework :: AsyncIO',
        'Framework :: Django',
        'Framework :: Flask',
        'Framework :: IDLE',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Framework :: Pyramid',
        'Framework :: Pytest',
        'Framework :: Robot Framework',
        'Framework :: Robot Framework :: Library',
        'Framework :: Robot Framework :: Tool',
        'Framework :: Scrapy',
        'Framework :: Setuptools Plugin',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Manufacturing',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: Android',
        'Operating System :: BeOS',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS 9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: Microsoft :: MS-DOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
        'Operating System :: Microsoft :: Windows :: Windows CE',
        'Operating System :: Microsoft :: Windows :: Windows NT/2000',
        'Operating System :: Microsoft :: Windows :: Windows Server 2003',
        'Operating System :: Microsoft :: Windows :: Windows Server 2008',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: OS Independent',
        'Operating System :: OS/2',
        'Operating System :: Other OS',
        'Operating System :: PDA Systems',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: AIX',
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: BSD/OS',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: GNU Hurd',
        'Operating System :: POSIX :: HP-UX',
        'Operating System :: POSIX :: IRIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: Other',
        'Operating System :: POSIX :: SCO',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: PalmOS',
        'Operating System :: Unix',
        'Operating System :: iOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Adaptive Technologies',
        'Topic :: Communications',
        'Topic :: Communications :: BBS',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Chat :: ICQ',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'Topic :: Communications :: Chat :: Unix Talk',
        'Topic :: Communications :: Conferencing',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Address Book',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
        'Topic :: Communications :: Email :: Filters',
        'Topic :: Communications :: Email :: Mail Transport Agents',
        'Topic :: Communications :: Email :: Mailing List Servers',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Communications :: FIDO',
        'Topic :: Communications :: Fax',
        'Topic :: Communications :: File Sharing',
        'Topic :: Communications :: Ham Radio',
        'Topic :: Communications :: Internet Phone',
        'Topic :: Communications :: Telephony',
        'Topic :: Communications :: Usenet News',
        'Topic :: Database',
        'Topic :: Desktop Environment',
        'Topic :: Documentation',
        'Topic :: Education',
        'Topic :: Education :: Testing',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Arcade',
        'Topic :: Games/Entertainment :: Board Games',
        'Topic :: Games/Entertainment :: First Person Shooters',
        'Topic :: Games/Entertainment :: Fortune Cookies',
        'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'Topic :: Games/Entertainment :: Real Time Strategy',
        'Topic :: Games/Entertainment :: Role-Playing',
        'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Games/Entertainment :: Turn Based Strategy',
        'Topic :: Home Automation',
        'Topic :: Internet',
        'Topic :: Internet :: File Transfer Protocol (FTP)',
        'Topic :: Internet :: Finger',
        'Topic :: Internet :: Log Analysis',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Internet :: Proxy Servers',
        'Topic :: Internet :: WAP',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Internet :: WWW/HTTP :: Session',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
        'Topic :: Internet :: XMPP',
        'Topic :: Internet :: Z39.50',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: 3D Modeling',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Multimedia :: Graphics :: Capture',
        'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
        'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
        'Topic :: Multimedia :: Graphics :: Editors',
        'Topic :: Multimedia :: Graphics :: Editors :: Raster-Based',
        'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Sound/Audio :: Analysis',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Playing',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping',
        'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Writing',
        'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
        'Topic :: Multimedia :: Sound/Audio :: Conversion',
        'Topic :: Multimedia :: Sound/Audio :: Editors',
        'Topic :: Multimedia :: Sound/Audio :: MIDI',
        'Topic :: Multimedia :: Sound/Audio :: Mixers',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
        'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
        'Topic :: Multimedia :: Sound/Audio :: Speech',
        'Topic :: Multimedia :: Video',
        'Topic :: Multimedia :: Video :: Capture',
        'Topic :: Multimedia :: Video :: Conversion',
        'Topic :: Multimedia :: Video :: Display',
        'Topic :: Multimedia :: Video :: Non-Linear Editor',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Artificial Life',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Security',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development',
        'Topic :: Software Development :: Bug Tracking',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Acceptance',
        'Topic :: Software Development :: Testing :: BDD',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: System',
        'Topic :: System :: Benchmark',
        'Topic :: System :: Boot',
        'Topic :: System :: Boot :: Init',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Filesystems',
        'Topic :: System :: Hardware',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking',
        'Topic :: System :: Networking :: Firewalls',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: System :: Networking :: Time Synchronization',
        'Topic :: System :: Operating System',
        'Topic :: System :: Power (UPS)',
        'Topic :: System :: Recovery Tools',
        'Topic :: System :: Shells',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: System Shells',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    keywords='threading thread multi-threading logging logger archiving tracing tracer debugging debugger automation csv txt markdown md YouTube videos URL scraping Selenium macos windows linux',


    # http://code.nabla.net/doc/setuptools/api/setuptools/setuptools.find_packages.html
    # https://stackoverflow.com/questions/51286928/what-is-where-argument-for-in-setuptools-find-packages
    packages=find_packages(exclude=['*dev*']),
    # packages=find_namespace_packages(include=['ship']),
    # package_dir={'':'src'},


    python_requires  = '>=3.6.*, <4',
    install_requires = [],  # Optional
    # https://packaging.python.org/discussions/install-requires-vs-requirements/


    # If there are data files included in your packages that need to be installed, specify them here.
    # If using Python 2.6 or earlier, then these have to be included in MANIFEST.in as well.
    package_data = {  # Optional
        # 'sample': ['package_data.dat'],
    },
    # Although 'package_data' is the preferred approach, in some case you may need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional


    # To provide executable scripts, use entry points in preference to the "scripts" keyword.
    # Entry points provide cross-platform support and allow `pip` to create the appropriate form of executable for the target platform.
    # For example, the following would provide a command called `save-thread-result` which executes the code in the module `__main__` from this package when invoked directly from the command line:
    # entry_points={  # Optional
    #    'console_scripts': [
    #        'save-thread-result=save-thread-result:__main__',
    #    ],
    # },


    project_urls = {
        'Bug Reports':   'https://github.com/slow-but-steady/save-thread-result/issues',
        'PyPi Funding':  'https://donate.pypi.org',
        'Source':        'https://github.com/slow-but-steady/save-thread-result/tree/main/python',
        'Pull requests': 'https://github.com/slow-but-steady/save-thread-result/pulls',
        'Issues':        'https://github.com/slow-but-steady/save-thread-result/issues',
        'Code':          'https://github.com/slow-but-steady/save-thread-result/tree/main/python'
    },
)

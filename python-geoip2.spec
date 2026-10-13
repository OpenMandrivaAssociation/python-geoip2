Name:		python-geoip2
Version:	2.9.0
Release:	2
Summary:	MaxMind GeoIP2 API
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/geoip2/
Source0:	geoip2-2.9.0.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(maxminddb)
BuildRequires:	python%{pyver}dist(requests)
BuildArch:	noarch
%description
MaxMind GeoIP2 API.

%files
%{py_sitedir}/*

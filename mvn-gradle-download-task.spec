#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-gradle-download-task
Version  : 3.4.3
Release  : 1
URL      : https://github.com/michel-kraemer/gradle-download-task/archive/3.4.3.tar.gz
Source0  : https://github.com/michel-kraemer/gradle-download-task/archive/3.4.3.tar.gz
Source1  : https://repo1.maven.org/maven2/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.jar
Source2  : https://repo1.maven.org/maven2/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-gradle-download-task-data = %{version}-%{release}
Requires: mvn-gradle-download-task-license = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
Gradle Download Task [![CircleCI](https://img.shields.io/circleci/project/michel-kraemer/gradle-download-task.svg)](https://circleci.com/gh/michel-kraemer/gradle-download-task) [![codecov](https://codecov.io/gh/michel-kraemer/gradle-download-task/branch/master/graph/badge.svg)](https://codecov.io/gh/michel-kraemer/gradle-download-task) [![Apache License, Version 2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)
====================

%package data
Summary: data components for the mvn-gradle-download-task package.
Group: Data

%description data
data components for the mvn-gradle-download-task package.


%package license
Summary: license components for the mvn-gradle-download-task package.
Group: Default

%description license
license components for the mvn-gradle-download-task package.


%prep
%setup -q -n gradle-download-task-3.4.3

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-gradle-download-task
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-gradle-download-task/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.jar
/usr/share/java/.m2/repository/de/undercouch/gradle-download-task/3.4.3/gradle-download-task-3.4.3.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-gradle-download-task/LICENSE.txt

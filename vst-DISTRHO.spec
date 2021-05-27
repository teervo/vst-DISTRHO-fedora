# There is no .debuginfo for these packages
%global debug_package %{nil}

%global github_release 2021-03-15
%global rel_tag 2021_05_26

Name:       vst-DISTRHO
Version:    0
Release:    0.1.%{rel_tag}%{?dist}
Summary:    Linux audio plugins ports
URL:		https://distrho.sourceforge.io/ports.php
License:    GPLv2 and GPLv3 and MIT
Source0:    https://github.com/DISTRHO/DISTRHO-Ports/archive/refs/tags/%{github_release}.tar.gz

# Use spectool -g -R DISTRHO-Ports.spec to download sources for local builæd

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xcursor)

%description
DISTRHO is an open source project with the goal of making cross-platform audio plugins and GNU/Linux + LV2 ports.

# Dexed

%package dexed
Summary:	Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7

%description dexed
Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7.
Dexed is also a midi cartridge librarian/manager for the DX7

# Vitalium

%package vitalium
Summary:	vitalium is a spectral warping wavetable synthesizer

%description vitalium
vitalium is the Open Source version of the Vital spectral warping wavetable synthesizer

%package TAL
Summary:	Misc Plugins for TAL (tal-filter, tal-filter-2, tal-noisemaker, tal-reverb, tal-reverb-2, tal-reverb-3, tal-vocoder-2)

# TAL

%description TAL
Misc Plugins for TAL (tal-filter, tal-filter-2, tal-noisemaker, tal-reverb, tal-reverb-2, tal-reverb-3, tal-vocoder-2)

%package dRowAudio
Summary:	Plugins from dRowAudio (distortion, distortionshaper, flanger, reverb, tremolo)

# dRowAudio

%description dRowAudio
Plugins from dRowAudio (distortion, distortionshaper, flanger, reverb, tremolo)


%package Arctican
Summary:	Arctican VST plugins

%description Arctican
Plugins from Arctican (The Functiom & The Pilgrim)

# LUFS

%package LUFS
Summary:	Klangfreund metering plugins (Multimeter + LUFS Meter)

%description LUFS
Klangfreund metering plugins (Multimeter + LUFS Meter)

# EasySSP

%package EasySSP
Summary:	Easy Sound Space Perception is a small and lightweight audio visualization tool

%description EasySSP
Easy Sound Space Perception is a small and lightweight audio visualization tool, which currently provides spectrometer and goniometer views.

# JuceOPL

%package JuceOPL
Summary:	Classic game sounds in Plugin form, as heard in late 80s / early 90s sound cards

%description JuceOPL
Classic game sounds in Plugin form, as heard in late 80s / early 90s sound cards.

# KlangFalter

%package KlangFalter
Summary:	KlangFalter is a convolution audio plugin

%description KlangFalter
KlangFalter is a convolution audio plugin

# Luftikus

%package Luftikus
Summary:	Luftikus VST plugin

%description Luftikus
Luftikus is a digital adaptation of an analog EQ with fixed half-octave bands and additional high frequency boost.
As an improvement to the hardware it allows deeper cuts and supports a keep-gain mode where overall gain changes are avoided.

# Obxd

%package Obxd
Summary:	Obxd is emulation of famous ob-x, ob-xa and ob8 synths

%description Obxd
Obxd is emulation of famous ob-x, ob-xa and ob8 synths.

# Refine

%package ReFine
Summary:	ReFine VST plugin

%description ReFine
ReFine is a plugin that allows to add a final polishing to your tracks, busses and masters.
It extracts psycho-acoustic parameters from the source and thus allows to add warmth, space and punch to your mixes.

# Wolpertinger

%package Wolpertinger
Summary:	Wolpertinger is a subtractive, antialiased polyphonic software synthesizer     

%description Wolpertinger
Wolpertinger is a subtractive, antialiased polyphonic software synthesizer.

# Vex

%package Vex
Summary:	Vex is a 3 oscillator subtractive waverom synth

%description Vex
Vex is a 3 oscillator subtractive waverom synth

# Temper
%package Temper
Summary:	Temper is a modern digital distortion plugin

%description Temper
Temper is a modern digital distortion plugin featuring a rich saturation stage and a unique phase distortion.
Use the variable saturation curve to add warmth and edge to your sound, and let the phase distortion bring character and clarity through your mix.
Temper also features a simple resonant lowpass filter and a feedback path to drive the intensity of the tone.


# SwankyAmp
%package SwankyAmp
Summary:	Swanky Amp is a tube amplifier emulation plug-in

%description SwankyAmp
Swanky Amp is a tube amplifier emulation plug-in which is based on detailed simulations of tube amplification.
Discover new tones effortlessly with intuitive controls, harnessing the coveted sounds of dynamic tube amplification.

# PitchedDelay
%package PitchedDelay
Summary:	PitchedDelay is a delay that allows the pitching the delayed signal

%description PitchedDelay
PitchedDelay is a delay that allows the pitching the delayed signal, within or outside the feedback loop.

# StereoSourceSeparation
%package StereoSourceSeparation
Summary:	Stereo Source Separation plugin

%description StereoSourceSeparation
This is a plugin that uses the spatial information hidden in the stereo signal to accomplish source separation.

# HiReSam

%package HiReSam
Summary:	Klangfreund High Resolution Spectrum Analyse Meter

%description HiReSam
Klangfreund High Resolution Spectrum Analyse Meter

# eqinox
%package eqinox
Summary:	EQinox equaliser plugin

%description eqinox
EQinox equaliser plugin

# drumsynth
%package drumsynth
Summary:	drumsynth VST plugin

%description drumsynth
drumsynth VST plugin

%prep
%autosetup -p1 -n DISTRHO-Ports-%{github_release}

%build
%meson -Dbuild-lv2=false -Dbuild-vst2=true -Dbuild-vst3=true
%meson_build

%install
%meson_install

# Remove LV2 and duplicate VS2 plugins
rm -rf %{buildroot}%{_libdir}/lv2
rm -rf %{buildroot}%{_libdir}/vst/SwankyAmp.so
rm -rf %{buildroot}%{_libdir}/vst/vitalium.so


%files dexed
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/Dexed.so

%files vitalium
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst3/vitalium.vst3/*

%files TAL
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/TAL-*.so

%files dRowAudio
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/drowaudio-*.so

%files Arctican
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/The*.so

%files LUFS
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/LUFSMeter*.so

%files EasySSP
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/EasySSP.so

%files JuceOPL
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/JuceOPL.so

%files KlangFalter
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/KlangFalter.so

%files Luftikus
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/Luftikus.so

%files drumsynth
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/drumsynth.so

%files eqinox
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/eqinox.so

%files HiReSam
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/HiReSam.so

%files Obxd
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/Obxd.so

%files PitchedDelay
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/PitchedDelay.so

%files ReFine
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/ReFine.so

%files StereoSourceSeparation
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/StereoSourceSeparation.so

%files SwankyAmp
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst3/SwankyAmp.vst3/*

%files Temper
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/Temper.so

%files Vex
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/vex.so

%files Wolpertinger
%doc README.md
%license doc/GPL.txt
%{_libdir}/vst/Wolpertinger.so

%changelog
* Tue Apr 27 2021 Tim Lauridsen <tla@rasmil.dk> 0-0.2.2021_03_15
- use pkgconfig() for build requirements
* Fri Apr 23 2021 Tim Lauridsen <tla@rasmil.dk> 0-0.1.2021_03_15
- Initial build

# DISTRHO-Ports VST plugin packages for Fedora

https://github.com/DISTRHO/DISTRHO-Ports

Based on [timlau's lv2 spec files](https://github.com/timlau/spec_files/tree/master/DISTRHO-Ports)

This repo is used to generate the Copr repo [teervo/DISTRHO](https://copr.fedorainfracloud.org/coprs/teervo/DISTRHO/).

To install, first enable the repository
```
sudo dnf copr enable teervo/helm-synth
```

Then use dnf to install one or more of the provided packages:

```
vst-DISTRHO-Arctican.x86_64 : Arctican VST plugins
vst-DISTRHO-EasySSP.x86_64 : Easy Sound Space Perception is a small and lightweight audio visualization tool
vst-DISTRHO-HiReSam.x86_64 : Klangfreund High Resolution Spectrum Analyse Meter
vst-DISTRHO-JuceOPL.x86_64 : Classic game sounds in Plugin form, as heard in late 80s / early 90s sound cards
vst-DISTRHO-KlangFalter.x86_64 : KlangFalter is a convolution audio plugin
vst-DISTRHO-LUFS.x86_64 : Klangfreund metering plugins (Multimeter + LUFS Meter)
vst-DISTRHO-Luftikus.x86_64 : Luftikus VST plugin
vst-DISTRHO-Obxd.x86_64 : Obxd is emulation of famous ob-x, ob-xa and ob8 synths
vst-DISTRHO-PitchedDelay.x86_64 : PitchedDelay is a delay that allows the pitching the delayed signal
vst-DISTRHO-ReFine.x86_64 : ReFine VST plugin
vst-DISTRHO-StereoSourceSeparation.x86_64 : Stereo Source Separation plugin
vst-DISTRHO-SwankyAmp.x86_64 : Swanky Amp is a tube amplifier emulation plug-in
vst-DISTRHO-TAL.x86_64 : Misc Plugins for TAL (tal-filter, tal-filter-2, tal-noisemaker, tal-reverb, tal-reverb-2, tal-reverb-3, tal-vocoder-2)
vst-DISTRHO-Temper.x86_64 : Temper is a modern digital distortion plugin
vst-DISTRHO-Vex.x86_64 : Vex is a 3 oscillator subtractive waverom synth
vst-DISTRHO-Wolpertinger.x86_64 : Wolpertinger is a subtractive, antialiased polyphonic software synthesizer
vst-DISTRHO-dRowAudio.x86_64 : Plugins from dRowAudio (distortion, distortionshaper, flanger, reverb, tremolo)
vst-DISTRHO-dexed.x86_64 : Dexed is a multi platform, multi format plugin synth that is closely modeled on the Yamaha DX7
vst-DISTRHO-drumsynth.x86_64 : drumsynth VST plugin
vst-DISTRHO-eqinox.x86_64 : EQinox equaliser plugin
vst-DISTRHO-vitalium.x86_64 : vitalium is a spectral warping wavetable synthesizer
```


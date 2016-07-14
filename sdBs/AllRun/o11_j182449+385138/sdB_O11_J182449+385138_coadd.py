from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[276.204167,38.860556],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_O11_J182449+385138/sdB_O11_J182449+385138_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_O11_J182449+385138/sdB_O11_J182449+385138_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

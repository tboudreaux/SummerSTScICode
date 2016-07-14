from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.707917,41.582778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J19028+4134/sdB_Kepler_J19028+4134_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J19028+4134/sdB_Kepler_J19028+4134_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

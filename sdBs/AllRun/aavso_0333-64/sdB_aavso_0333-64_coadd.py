from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[53.642542,-64.015667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_aavso_0333-64/sdB_aavso_0333-64_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_aavso_0333-64/sdB_aavso_0333-64_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[39.058667,43.740444],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0232+435/sdB_FBS_0232+435_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0232+435/sdB_FBS_0232+435_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

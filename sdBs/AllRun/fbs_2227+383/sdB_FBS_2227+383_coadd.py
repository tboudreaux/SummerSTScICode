from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[337.318417,38.617778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_2227+383/sdB_FBS_2227+383_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_2227+383/sdB_FBS_2227+383_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[300.467542,-71.956992],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_19563-7205/sdB_EC_19563-7205_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_19563-7205/sdB_EC_19563-7205_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

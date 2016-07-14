from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[294.635833,46.066389],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_2m1938+4603/sdB_kepler_2m1938+4603_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_2m1938+4603/sdB_kepler_2m1938+4603_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

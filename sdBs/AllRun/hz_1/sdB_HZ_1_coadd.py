from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[72.556292,17.701717],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HZ_1/sdB_HZ_1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HZ_1/sdB_HZ_1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

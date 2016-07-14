from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[327.157125,-76.345767],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_87/sdB_JL_87_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_87/sdB_JL_87_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

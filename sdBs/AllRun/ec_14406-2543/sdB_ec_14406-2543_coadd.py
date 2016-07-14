from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[220.884542,-25.933028],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_14406-2543/sdB_ec_14406-2543_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_14406-2543/sdB_ec_14406-2543_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

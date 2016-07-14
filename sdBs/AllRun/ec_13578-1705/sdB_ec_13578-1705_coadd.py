from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[210.145208,-17.339625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_13578-1705/sdB_ec_13578-1705_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_13578-1705/sdB_ec_13578-1705_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

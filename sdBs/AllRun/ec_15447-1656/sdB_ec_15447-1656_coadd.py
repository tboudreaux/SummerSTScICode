from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[236.893042,-17.094614],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_15447-1656/sdB_ec_15447-1656_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_15447-1656/sdB_ec_15447-1656_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

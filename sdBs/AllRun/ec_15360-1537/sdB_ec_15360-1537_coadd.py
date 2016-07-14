from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[234.728542,-15.780206],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_15360-1537/sdB_ec_15360-1537_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_15360-1537/sdB_ec_15360-1537_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

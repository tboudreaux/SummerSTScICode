from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[197.430917,-27.926669],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_13069-2739/sdB_ec_13069-2739_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_13069-2739/sdB_ec_13069-2739_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

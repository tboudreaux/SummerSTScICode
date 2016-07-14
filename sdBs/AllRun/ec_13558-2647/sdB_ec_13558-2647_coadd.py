from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[209.662417,-27.041383],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_13558-2647/sdB_ec_13558-2647_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_13558-2647/sdB_ec_13558-2647_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

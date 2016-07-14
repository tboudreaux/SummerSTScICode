from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[303.769917,-40.095619],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_20117-4014/sdB_ec_20117-4014_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_20117-4014/sdB_ec_20117-4014_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

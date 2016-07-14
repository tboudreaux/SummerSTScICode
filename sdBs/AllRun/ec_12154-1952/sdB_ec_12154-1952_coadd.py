from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[184.501,-20.149042],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_12154-1952/sdB_ec_12154-1952_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_12154-1952/sdB_ec_12154-1952_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[228.292667,-16.139264],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_15103-1557/sdB_EC_15103-1557_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_15103-1557/sdB_EC_15103-1557_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

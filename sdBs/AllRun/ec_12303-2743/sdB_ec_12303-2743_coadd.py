from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[188.248417,-28.005194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_ec_12303-2743/sdB_ec_12303-2743_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_ec_12303-2743/sdB_ec_12303-2743_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

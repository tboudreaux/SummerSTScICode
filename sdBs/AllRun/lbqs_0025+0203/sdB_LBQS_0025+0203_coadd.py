from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[7.027958,2.338331],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LBQS_0025+0203/sdB_LBQS_0025+0203_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LBQS_0025+0203/sdB_LBQS_0025+0203_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

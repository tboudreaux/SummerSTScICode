from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[96.968833,42.779278],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0624+428/sdB_fbs_0624+428_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0624+428/sdB_fbs_0624+428_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

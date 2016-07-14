from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[105.47375,34.966361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_fbs_0658+350/sdB_fbs_0658+350_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_fbs_0658+350/sdB_fbs_0658+350_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

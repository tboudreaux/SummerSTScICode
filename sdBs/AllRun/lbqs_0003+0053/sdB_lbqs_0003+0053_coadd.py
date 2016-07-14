from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[1.594292,1.166369],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_lbqs_0003+0053/sdB_lbqs_0003+0053_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_lbqs_0003+0053/sdB_lbqs_0003+0053_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[83.420417,23.090667],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kuv_05306+2303/sdB_kuv_05306+2303_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kuv_05306+2303/sdB_kuv_05306+2303_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

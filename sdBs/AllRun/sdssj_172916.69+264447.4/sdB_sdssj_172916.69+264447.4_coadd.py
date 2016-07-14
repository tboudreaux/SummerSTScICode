from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[262.319542,26.7465],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_172916.69+264447.4/sdB_sdssj_172916.69+264447.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_172916.69+264447.4/sdB_sdssj_172916.69+264447.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[218.332958,-1.909611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_143319.91-015434.6/sdB_SDSSJ910_143319.91-015434.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_143319.91-015434.6/sdB_SDSSJ910_143319.91-015434.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

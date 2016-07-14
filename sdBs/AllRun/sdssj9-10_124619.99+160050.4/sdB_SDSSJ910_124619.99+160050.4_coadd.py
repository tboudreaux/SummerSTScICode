from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[191.583292,16.014],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_124619.99+160050.4/sdB_SDSSJ910_124619.99+160050.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_124619.99+160050.4/sdB_SDSSJ910_124619.99+160050.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

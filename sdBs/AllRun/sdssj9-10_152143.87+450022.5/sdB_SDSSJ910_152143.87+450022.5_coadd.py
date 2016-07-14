from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[230.432792,45.00625],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_152143.87+450022.5/sdB_SDSSJ910_152143.87+450022.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_152143.87+450022.5/sdB_SDSSJ910_152143.87+450022.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()

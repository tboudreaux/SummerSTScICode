from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[246.674958,40.488056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_162641.99+402917.0/sdB_sdssj9-10_162641.99+402917.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_162641.99+402917.0/sdB_sdssj9-10_162641.99+402917.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
